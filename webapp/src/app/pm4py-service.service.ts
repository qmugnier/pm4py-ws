import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class Pm4pyService {
  webservicePath: string;

  constructor(private http: HttpClient) {
    this.webservicePath = "http://localhost:5000/";
  }

  getProcessSchema(parameters={}) {
    var completeUrl : string = this.webservicePath + "getProcessSchema";
    //return this.http.get(completeUrl);
    return this.http.request("GET",completeUrl,{responseType:"json"});
  }
}
