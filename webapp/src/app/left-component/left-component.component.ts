import { Component, OnInit } from '@angular/core';
import {StartActivitiesFilterComponent} from "../start-activities-filter/start-activities-filter.component";
import {EndActivitiesFilterComponent} from "../end-activities-filter/end-activities-filter.component";
import {VariantsFilterComponent} from "../variants-filter/variants-filter.component";
import {FilterServiceService} from "../filter-service.service";
import {AttributesFilterComponent} from "../attributes-filter/attributes-filter.component";
import {MatDialog} from '@angular/material';
import {Pm4pyService} from "../pm4py-service.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-left-component',
  templateUrl: './left-component.component.html',
  styleUrls: ['./left-component.component.scss']
})
export class LeftComponentComponent implements OnInit {
  filterService : FilterServiceService;
  router: Router;
  public dialog : MatDialog;
  public processProvided: boolean;

  constructor(public _dialog: MatDialog, public _filterService : FilterServiceService, private _route: Router) {
    this.filterService = _filterService;
    this.filterService.retrieveFiltersFromLocalStorage();
    this.dialog = _dialog;
    this.router = _route;
    this.router.events.subscribe((val) => {
      let process_name: string = localStorage.getItem("process");
      if (process_name != null) {
        if (this.router.url === "/logsList" || this.router.url === "/logsList2") {
          this.processProvided = false;
        }
        else if (this.router.url == "/login") {
          this.processProvided = false;
        }
        else {
          this.processProvided = true;
        }
      }
      else {
        this.processProvided = false;
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
    } else {
      this.processProvided = false;
    }
  }

  startActivitiesFilter() {
    this.dialog.open(StartActivitiesFilterComponent);
  }

  endActivitiesFilter() {
    this.dialog.open(EndActivitiesFilterComponent);
  }

  variantsFilter() {
    this.dialog.open(VariantsFilterComponent);
  }

  attributesFilter() {
    this.dialog.open(AttributesFilterComponent);
  }

}
