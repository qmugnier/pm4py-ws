import { Component, OnInit } from '@angular/core';
import { FilterServiceService } from '../filter-service.service';
import {Router} from "@angular/router";

@Component({
  selector: 'app-filters',
  templateUrl: './filters.component.html',
  styleUrls: ['./filters.component.scss']
})
export class FiltersComponent implements OnInit {
  public filterService : FilterServiceService;
  public filters : any;

  constructor(public _filterService : FilterServiceService, private _route: Router) {
    /**
     * Constructor
     */
    this.filterService = _filterService;
    this.getFilters();
    _route.events.subscribe((val) => {
      this.getFilters();
    });
  }

  ngOnInit() {
    /**
     * Manages the initialization of the component
     */
  }

  public getFilters() {
    this.filters = this.filterService.getFilters();
  }

}
