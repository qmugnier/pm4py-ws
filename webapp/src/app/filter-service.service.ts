import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class FilterServiceService {
  filtersPerProcess : any;
  thisProcess : string;

  constructor() {
    this.filtersPerProcess = localStorage.getItem("filtersPerProcess");
    if (this.filtersPerProcess == null) {
      this.filtersPerProcess = new Object();
    }
    else {
      this.filtersPerProcess = JSON.parse(this.filtersPerProcess);
    }
    this.thisProcess = localStorage.getItem("process");
    if (!(this.thisProcess in this.filtersPerProcess)) {
      this.filtersPerProcess[this.thisProcess] = [];
    }
  }

  retrieveFiltersFromLocalStorage() {
    this.filtersPerProcess = localStorage.getItem("filtersPerProcess");
    if (this.filtersPerProcess == null) {
      this.filtersPerProcess = new Object();
    }
    else {
      this.filtersPerProcess = JSON.parse(this.filtersPerProcess);
    }
    this.thisProcess = localStorage.getItem("process");
    if (!(this.thisProcess in this.filtersPerProcess)) {
      this.filtersPerProcess[this.thisProcess] = [];
    }
  }

  addFilter(filter_type : string, filter_value : any) {
    let process : string = localStorage.getItem("process");
    this.filtersPerProcess[process].push([filter_type, filter_value]);
    localStorage.setItem("filtersPerProcess", JSON.stringify(this.filtersPerProcess));
    console.log("SUCCESS!");
    console.log(this.filtersPerProcess);
  }

  remove(filter) {
    console.log("REMOVE");
    console.log(filter);
    let thisIndex : number = this.filtersPerProcess[this.thisProcess].indexOf(filter, 0);
    this.filtersPerProcess[this.thisProcess].splice(thisIndex, 1);
    localStorage.setItem("filtersPerProcess", JSON.stringify(this.filtersPerProcess));
  }

  getFilters() {
    return this.filtersPerProcess[this.thisProcess];
  }
}
