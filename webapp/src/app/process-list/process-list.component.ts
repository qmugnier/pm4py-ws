import { Component, OnInit } from '@angular/core';
import {Pm4pyService} from "../pm4py-service.service";
import {HttpParams} from "@angular/common/http";
import {Router} from "@angular/router";

@Component({
  selector: 'app-process-list',
  templateUrl: './process-list.component.html',
  styleUrls: ['./process-list.component.scss']
})
export class ProcessListComponent implements OnInit {
  pm4pyService: Pm4pyService;
  logsListJson: JSON;
  router : Router;
  public logsList: string[];

  constructor(private pm4pyServ: Pm4pyService, private _route : Router) {
    /**
     * Constructor
     */
    this.pm4pyService = pm4pyServ;
    this.router = _route;
    this.getProcessList();
  }

  getProcessList() {
    /**
     * Gets the list of processes loaded into the service
     */
    let params: HttpParams = new HttpParams();

    this.pm4pyService.getLogsList(params).subscribe(data => {
      this.logsListJson = data as JSON;
      this.logsList = this.logsListJson["logs"];
    });
  }

  ngOnInit() {
    /**
     * Manages the initialization of the component
     */
    localStorage.removeItem("process");
  }

  logClicked(log) {
    /**
     * Manages the click on a process
     */
    localStorage.setItem("process", log);
    this.router.navigate(["/process"]);
  }

}
