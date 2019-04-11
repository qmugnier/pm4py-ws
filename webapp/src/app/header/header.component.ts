import {Component, OnInit} from '@angular/core';
import {Router} from "@angular/router";
import { environment } from '../../environments/environment';
import {HttpParams} from "@angular/common/http";
import {DomSanitizer} from "@angular/platform-browser";
import {Pm4pyService} from "../pm4py-service.service";
import {MatDialog} from '@angular/material';
import {StartActivitiesFilterComponent} from "../start-activities-filter/start-activities-filter.component";

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  public processProvided: boolean;
  router: Router;
  public title: string;
  public helpString: string = "";
  public enableDownload : boolean = false;
  public enableUpload : boolean = false;
  sanitizer: DomSanitizer;
  pm4pyService: Pm4pyService;
  isNotLogin : boolean = true;
  loginEnabled : boolean = true;
  public dialog : MatDialog;

  userId: string;

  public logsListHelpString: string = "This page contains a list of logs loaded in the system. To open one of them click on the name of the log.";


  constructor(private _route: Router, private _sanitizer: DomSanitizer, private pm4pyServ: Pm4pyService, public _dialog: MatDialog) {
    /**
     * Constructor (initialize the title and the help of the single page)
     */
    this.pm4pyService = pm4pyServ;
    this.sanitizer = _sanitizer;
    this.dialog = _dialog;
    this.enableDownload = environment.enableDownload;
    this.enableUpload = environment.enableUpload;
    this.title = "PM4Py WI";
    this.router = _route;
    this.loginEnabled = environment.enableLogin;
    this.router.events.subscribe((val) => {
      let process_name: string = localStorage.getItem("process");
      if (process_name != null) {
        this.title = "PM4Py WI";
        this.helpString = "";
        if (this.router.url === "/logsList") {
          this.isNotLogin = true;
          this.processProvided = false;
          this.title = "PM4Py WI - List of Logs";
          this.helpString = this.logsListHelpString;
        }
        else if (this.router.url == "/login") {
          this.title = "PM4Py WI - Login";
          this.helpString = "Insert your username and password to enter the application";
          this.processProvided = false;
          this.enableDownload = false;
          this.enableUpload = false;
          this.isNotLogin = false;
        }
        else {
          this.processProvided = true;
          this.isNotLogin = true;
          if (this.router.url === "/process") {
            this.title = "PM4Py WI - Process Discovery" + " (" + process_name + ")";
            this.helpString = "This page shows the process discovered by our algorithms on the given log. You can change the discovery algorithm" +
              "by going on the 'Type of model' selection. You can also choose the level of simplicity of the output model (an automatic filtering is done). You can" +
              " choose frequency or performance decoration. The progress bars represents how many variants, cases and events have been selected by the current" +
              " set of filters";
          } else if (this.router.url === "/sna") {
            this.title = "PM4Py WI - Social Network Analysis" + " (" + process_name + ")";
            this.helpString = "This page shows the Social Network discovered by our algorithms on the given log. You can change the metric by going on the" +
              " 'Metric' selection. You can also change the threshold used to filter out arcs in the visualization.";
            ;
          } else if (this.router.url === "/cases") {
            this.title = "PM4Py WI - Case Management" + " (" + process_name + ")";
            this.helpString = "This page shows the variants, cases and events of the given log. Clicking on a variant, you can restrict the view to the cases" +
              " belonging to that variant. Clicking on a case, you can see the events belonging to the case.";
          } else if (this.router.url === "/statistics") {
            this.title = "PM4Py WI - Statistics" + " (" + process_name + ")";
            this.helpString = "This page shows the 'Events per time' (the distribution of events over time) and the 'Case duration' (the distribution of the duration" +
              " of the single cases) graphs.";
          } else if (this.router.url === "/simulation") {
            this.title = "PM4Py WI - Simulation" + " (" + process_name + ")";
            this.helpString = "Perform transient simulation of the process at the specified delay from the start time (it gives a probability distribution over states of the process).";
          } else if (this.router.url == "/alignments") {
            this.title = "PM4Py WI - Alignments (" + process_name + ")";
            this.helpString = "Perform alignments between the log and the reference model that was selected. Two tabs are provided, one containing the projection of the alignments on the model and one reporting a table of the alignments.";
          }
        }
      } else {
        this.processProvided = false;
        if (environment.enableLogin) {
          this.title = "PM4Py WI - Login";
          this.helpString = "Insert your username and password to enter the application";
          this.processProvided = false;
          this.enableDownload = false;
          this.enableUpload = false;
          this.isNotLogin = false;
        }
        else {
          this.title = "PM4Py WI - List of Logs";
          this.isNotLogin = true;
          this.helpString = this.logsListHelpString;
        }
      }
      this.checkSession();
    });
  }

  ngOnInit() {
    /**
     * Manages the initialization of the component
     */
    this.processProvided = false;
    let process_name: string = localStorage.getItem("process");
    if (process_name != null) {
      this.processProvided = true;
      this.title = "PM4Py WI" + " (" + process_name + ")";
      ;
    } else {
      this.processProvided = false;
    }
  }

  downloadFile(data: string, type: string) {
    const blob = new Blob([data], { type: type });
    const url= window.URL.createObjectURL(blob);
    window.open(url);
  }

  downloadCsv() {
    let httpParams : HttpParams = new HttpParams();

    this.pm4pyService.downloadCsvLog(httpParams).subscribe(data => {
      let csvJson : JSON = data as JSON;
      this.downloadFile(csvJson['content'], 'text/csv');
    });
  }

  downloadXes() {
    let httpParams : HttpParams = new HttpParams();

    this.pm4pyService.downloadXesLog(httpParams).subscribe(data => {
      let xesJson : JSON = data as JSON;
      this.downloadFile(xesJson['content'], 'text/csv');
    });
  }

  uploadFile($event) {
    let reader = new FileReader();
    let filename : string = $event.target.files[0].name;
    let filetype : string = $event.target.files[0].type;
    let extension : string = filename.split(".")[1];
    if (extension === "xes") {
      reader.readAsDataURL($event.target.files[0]);
      reader.onload = () => {
        let base64: string = reader.result.toString();
        let data : any = {"filename": filename, "base64": base64};
        this.pm4pyService.uploadLog(data, new HttpParams()).subscribe(data => {
          let responseJson : JSON = data as JSON;
          if (responseJson["status"] === "OK") {
            window.location.reload();
          }
          else {
            alert("Something has gone wrong in the upload!");
          }
        })
      }
    }
    else {
      alert("unsupported file type for direct upload!")
    }
  }

  checkSession() {
    let httpParams : HttpParams = new HttpParams();

    this.pm4pyService.checkSessionService(httpParams).subscribe(data => {
      let sessionJson : JSON = data as JSON;

      if ("user" in sessionJson) {
        this.userId = sessionJson["user"];
        this.isNotLogin = true;
      }

      if ("can_upload" in sessionJson) {
        this.enableUpload = environment.enableUpload && sessionJson["can_upload"] && this.isNotLogin;
      }

      if ("can_download" in sessionJson) {
        this.enableDownload = environment.enableDownload && sessionJson["can_download"] && this.isNotLogin;
      }
    })
  }

  doLogout() {
    localStorage.removeItem("process");
    localStorage.removeItem("sessionId");
    this.router.navigateByUrl("/login");
    window.location.reload();
  }

  startActivitiesFilter() {
    this.dialog.open(StartActivitiesFilterComponent);
  }

}
