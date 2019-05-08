import { Component, OnInit } from '@angular/core';
import {FilterServiceService} from "../filter-service.service";
import {MatDialog} from "@angular/material";
import {StartActivitiesFilterComponent} from "../start-activities-filter/start-activities-filter.component";
import {EndActivitiesFilterComponent} from "../end-activities-filter/end-activities-filter.component";
import {VariantsFilterComponent} from "../variants-filter/variants-filter.component";
import {AttributesFilterComponent} from "../attributes-filter/attributes-filter.component";

@Component({
  selector: 'app-all-filters',
  templateUrl: './all-filters.component.html',
  styleUrls: ['./all-filters.component.scss']
})
export class AllFiltersComponent implements OnInit {
  filterService : FilterServiceService;
  public dialog : MatDialog;

  constructor(public _dialog: MatDialog, public _filterService : FilterServiceService) {
    this.filterService = _filterService;
    this.filterService.retrieveFiltersFromLocalStorage();
    this.dialog = _dialog;
  }

  ngOnInit() {
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
