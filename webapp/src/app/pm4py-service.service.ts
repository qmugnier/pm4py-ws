import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class Pm4pyService {
  webservicePath: string;

  constructor(private http: HttpClient) {
    /**
     * Constructor: initialize the web service path
     */
    this.webservicePath = "http://localhost:5000/";
  }

  getProcessSchema(parameters: HttpParams) {
    /**
     * Gets the process schema (with the provided parameters)
     *
     * Parameters:
     * parameters: HttpParams -> Parameters to pass in GET to the service
     *
     * Returns:
     * observer object
     */
    let process = localStorage.getItem("process");
    parameters = parameters.set("process", process);

    var completeUrl : string = this.webservicePath + "getProcessSchema";

    return this.http.get(completeUrl,{params: parameters});
  }

  getEventsPerTime(parameters: HttpParams) {
    /**
     * Gets the events per time graph
     *
     * Parameters:
     * parameters: HttpParams -> Parameters to pass in GET to the service
     *
     * Returns:
     * observer object
     */
    let process = localStorage.getItem("process");
    parameters = parameters.set("process", process);

    var completeUrl : string = this.webservicePath + "getEventsPerTimeGraph";

    return this.http.get(completeUrl,{params: parameters});
  }

  getCaseDurationGraph(parameters: HttpParams) {
    /**
     * Gets the case duration graph
     *
     * Parameters:
     * parameters: HttpParams -> Parameters to pass in GET to the service
     *
     * Returns:
     * observer object
     */
    let process = localStorage.getItem("process");
    parameters = parameters.set("process", process);

    var completeUrl : string = this.webservicePath + "getCaseDurationGraph";

    return this.http.get(completeUrl, {params: parameters});
  }

  getLogsList(parameters : HttpParams) {
    /**
     * Gets the list of logs loaded in the service
     *
     * Parameters:
     * parameters: HttpParams -> Parameters to pass in GET to the service
     *
     * Returns:
     * observer object
     */
    var completeUrl : string = this.webservicePath + "getLogsList";

    return this.http.get(completeUrl, {params: parameters});
  }

  transientAnalysis(parameters : HttpParams) {
    /**
     * Perform transient analysis of the given process
     *
     * Parameters:
     * parameters: HttpParams -> Parameters to pass in GET to the service
     *
     * Returns:
     * observer object
     */
    let process = localStorage.getItem("process");
    parameters = parameters.set("process", process);

    var completeUrl : string = this.webservicePath + "transientAnalysis";

    return this.http.get(completeUrl, {params: parameters});
  }

  getAllVariants(parameters : HttpParams) {
    /**
     * Gets all the variants from the given log
     *
     * Parameters:
     * parameters: HttpParams -> Parameters to pass in GET to the service
     *
     * Returns:
     * observer object
     */
    let process = localStorage.getItem("process");
    parameters = parameters.set("process", process);

    var completeUrl : string = this.webservicePath + "getAllVariants";

    return this.http.get(completeUrl, {params: parameters});
  }

  getAllCases(parameters : HttpParams) {
    /**
     * Gets all the cases from the given log
     *
     * Parameters:
     * parameters: HttpParams -> Parameters to pass in GET to the service
     *
     * Returns:
     * observer object
     */
    let process = localStorage.getItem("process");
    parameters = parameters.set("process", process);

    var completeUrl : string = this.webservicePath + "getAllCases";

    return this.http.get(completeUrl, {params: parameters});
  }

  getEvents(parameters : HttpParams) {
    /**
     * Gets all the events of a case in the given log
     *
     * Parameters:
     * parameters: HttpParams -> Parameters to pass in GET to the service
     *
     * Returns:
     * observer object
     */
    let process = localStorage.getItem("process");
    parameters = parameters.set("process", process);

    var completeUrl : string = this.webservicePath + "getEvents";

    return this.http.get(completeUrl, {params: parameters});
  }

  getServicePath() {
    /**
     * Gets the service path
     *
     * Returns:
     * service path
     */
    return this.webservicePath;
  }
}
