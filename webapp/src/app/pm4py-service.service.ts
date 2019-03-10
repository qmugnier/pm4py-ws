import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class Pm4pyService {
  webservicePath: string;

  constructor(private http: HttpClient) {
    this.webservicePath = "http://localhost:5000/";
  }

  getProcessSchema(parameters: HttpParams) {
    let process = localStorage.getItem("process");
    parameters = parameters.set("process", process);

    var completeUrl : string = this.webservicePath + "getProcessSchema";

    return this.http.get(completeUrl,{params: parameters});
  }

  getEventsPerTime(parameters: HttpParams) {
    let process = localStorage.getItem("process");
    parameters = parameters.set("process", process);

    var completeUrl : string = this.webservicePath + "getEventsPerTimeGraph";

    return this.http.get(completeUrl,{params: parameters});
  }

  getCaseDurationGraph(parameters: HttpParams) {
    let process = localStorage.getItem("process");
    parameters = parameters.set("process", process);

    var completeUrl : string = this.webservicePath + "getCaseDurationGraph";

    return this.http.get(completeUrl, {params: parameters});
  }

  getServicePath() {
    return this.webservicePath;
  }
}
