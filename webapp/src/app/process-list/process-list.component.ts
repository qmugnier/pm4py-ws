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
    this.pm4pyService = pm4pyServ;
    this.router = _route;
    this.getProcessList();
  }

  getProcessList() {
    let params: HttpParams = new HttpParams();

    this.pm4pyService.getLogsList(params).subscribe(data => {
      this.logsListJson = data as JSON;
      this.logsList = this.logsListJson["logs"];
      console.log(this.logsList);
    });
  }

  ngOnInit() {
    localStorage.removeItem("process");
  }

  logClicked(log) {
    localStorage.setItem("process", log);
    let currentUrl = this.router.url;
    this.router.navigate(["/process"]);
    window.location.reload();
  }

}
