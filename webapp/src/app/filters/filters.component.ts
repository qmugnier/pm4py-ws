import { Component, OnInit } from '@angular/core';
import { FilterServiceService } from '../filter-service.service';

@Component({
  selector: 'app-filters',
  templateUrl: './filters.component.html',
  styleUrls: ['./filters.component.scss']
})
export class FiltersComponent implements OnInit {
  public filterService : FilterServiceService;

  constructor(public _filterService : FilterServiceService) {
    /**
     * Constructor
     */
    this.filterService = _filterService;
  }

  ngOnInit() {
    /**
     * Manages the initialization of the component
     */
  }

  public getFilters() {
    return this.filterService.getFilters();
  }

}
