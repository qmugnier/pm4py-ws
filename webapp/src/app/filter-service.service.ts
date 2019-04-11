import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class FilterServiceService {
  filtersPerProcess : any;
  thisProcess : string;

  constructor() {
    this.thisProcess = localStorage.getItem("process");
    this.filtersPerProcess =  new Object();
    if (!(this.thisProcess in this.filtersPerProcess)) {
      this.filtersPerProcess[this.thisProcess] = [];
    }
  }

  addFilter(filter_type : string, filter_value : any) {
    let process : string = localStorage.getItem("process");
    this.filtersPerProcess[process].push([filter_type, filter_value]);
    console.log("SUCCESS!");
    console.log(this.filtersPerProcess);
  }

  remove(filter) {
    console.log("REMOVE");
    console.log(filter);
  }

  getFilters() {
    return this.filtersPerProcess[this.thisProcess];
  }
}
