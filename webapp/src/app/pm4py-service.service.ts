import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import { environment } from '../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class Pm4pyService {
  webservicePath: string;

  constructor(private http: HttpClient) {
    /**
     * Constructor: initialize the web service path
     */
    this.webservicePath = environment.webServicePath;
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
    let sessionId = localStorage.getItem("sessionId");

    parameters = parameters.set("process", process);
    parameters = parameters.set("sessionId", sessionId);

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
    let sessionId = localStorage.getItem("sessionId");

    parameters = parameters.set("process", process);
    parameters = parameters.set("sessionId", sessionId);

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
    let sessionId = localStorage.getItem("sessionId");

    parameters = parameters.set("process", process);
    parameters = parameters.set("sessionId", sessionId);

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

    let sessionId = localStorage.getItem("sessionId");
    parameters = parameters.set("sessionId", sessionId);

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
    let sessionId = localStorage.getItem("sessionId");

    parameters = parameters.set("process", process);
    parameters = parameters.set("sessionId", sessionId);

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
    let sessionId = localStorage.getItem("sessionId");

    parameters = parameters.set("process", process);
    parameters = parameters.set("sessionId", sessionId);

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
    let sessionId = localStorage.getItem("sessionId");

    parameters = parameters.set("process", process);
    parameters = parameters.set("sessionId", sessionId);

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
    let sessionId = localStorage.getItem("sessionId");

    parameters = parameters.set("process", process);
    parameters = parameters.set("sessionId", sessionId);

    var completeUrl : string = this.webservicePath + "getEvents";

    return this.http.get(completeUrl, {params: parameters});
  }

  getLogSummary(parameters : HttpParams) {
    /**
     * Gets the log summary
     *
     * Parameters:
     * parameters: HttpParams -> Parameters to pass in GET to the service
     *
     * Returns:
     * observer object
     */
    let process = localStorage.getItem("process");
    let sessionId = localStorage.getItem("sessionId");

    parameters = parameters.set("process", process);
    parameters = parameters.set("sessionId", sessionId);

    var completeUrl : string = this.webservicePath + "getLogSummary";

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

  getAlignmentsVisualizations(model : string, parameters : HttpParams) {
    let process = localStorage.getItem("process");
    let sessionId = localStorage.getItem("sessionId");

    parameters = parameters.set("process", process);
    parameters = parameters.set("sessionId", sessionId);

    var completeUrl : string = this.webservicePath + "getAlignmentsVisualizations";

    return this.http.post(completeUrl, {"model": model}, {params: parameters});
  }

  downloadCsvLog(parameters : HttpParams) {
    let process = localStorage.getItem("process");
    let sessionId = localStorage.getItem("sessionId");

    parameters = parameters.set("process", process);
    parameters = parameters.set("sessionId", sessionId);

    var completeUrl : string = this.webservicePath + "downloadCsvLog";

    return this.http.get(completeUrl, {params: parameters});
  }

  downloadXesLog(parameters : HttpParams) {
    let process = localStorage.getItem("process");
    let sessionId = localStorage.getItem("sessionId");

    parameters = parameters.set("process", process);
    parameters = parameters.set("sessionId", sessionId);

    var completeUrl : string = this.webservicePath + "downloadXesLog";

    return this.http.get(completeUrl, {params: parameters});
  }
}
