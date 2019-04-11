import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-filters',
  templateUrl: './filters.component.html',
  styleUrls: ['./filters.component.scss']
})
export class FiltersComponent implements OnInit {
  public filtersPerProcess : any;

  constructor() {
    /**
     * Constructor
     */
    this.filtersPerProcess =  new Object();
    let process : string = localStorage.getItem("process");
    if (!(process in this.filtersPerProcess)) {
      this.filtersPerProcess[process] = [];
    }
  }

  public addFilter(filter_type : string, filter_value : any) {
    let process : string = localStorage.getItem("process");
    this.filtersPerProcess[process].push([filter_type, filter_value]);
    console.log("SUCCESS!");
    console.log(this.filtersPerProcess);
  }

  ngOnInit() {
    /**
     * Manages the initialization of the component
     */
  }

}
