import {Component, OnInit} from '@angular/core';
import {Router} from "@angular/router";

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
  public logsListHelpString: string = "This page contains a list of logs loaded in the system. To open one of them click on the name of the log.";


  constructor(private _route: Router) {
    /**
     * Constructor (initialize the title and the help of the single page)
     */
    this.title = "PM4Py WI";
    this.router = _route;
    this.router.events.subscribe((val) => {
      let process_name: string = localStorage.getItem("process");
      if (process_name != null) {
        this.title = "PM4Py WI";
        this.helpString = "";
        if (this.router.url === "/logsList") {
          this.processProvided = false;
          this.title = "PM4Py WI - List of Logs";
          this.helpString = this.logsListHelpString;
        } else {
          this.processProvided = true;
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
          }
        }
      } else {
        this.processProvided = false;
        this.title = "PM4Py WI - List of Logs";
        this.helpString = this.logsListHelpString;
      }
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

}
