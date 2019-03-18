import { Component, OnInit } from '@angular/core';
import {DomSanitizer} from "@angular/platform-browser";
import {Pm4pyService} from "../pm4py-service.service";
import {HttpParams} from "@angular/common/http";
import { MatTableDataSource } from '@angular/material/table';

interface Variant {
  variant: string;
  count: number;
}

@Component({
  selector: 'app-cases',
  templateUrl: './cases.component.html',
  styleUrls: ['./cases.component.scss']
})
export class CasesComponent implements OnInit {
  public isLoading: boolean;
  public variantsLoading : boolean;
  public casesLoading : boolean;
  sanitizer: DomSanitizer;
  pm4pyService: Pm4pyService;
  pm4pyJsonVariants : JSON;
  variants : any[];
  displayedColumnsVariants : string[] = ["variant", "count"];
  dataSourceVariants = new MatTableDataSource<any>();



  constructor(private _sanitizer: DomSanitizer, private pm4pyServ: Pm4pyService) {
    /**
     * Constructor
     */
    this.sanitizer = _sanitizer;
    this.pm4pyService = pm4pyServ;
    this.variantsLoading = false;
    this.casesLoading = false;
    this.isLoading = false;

    this.getAllVariants();
  }

  ngOnInit() {
    /**
     * Manages the initialization of the component
     */
  }

  getAllVariants() {
    this.variantsLoading = true;
    this.isLoading = this.variantsLoading || this.casesLoading;
    let params: HttpParams = new HttpParams();
    this.pm4pyService.getAllVariants(params).subscribe(data => {
      this.pm4pyJsonVariants = data as JSON;
      console.log(this.pm4pyJsonVariants);
      this.variants = this.pm4pyJsonVariants["variants"];
      let i : number = 0;
      while (i < this.variants.length) {
        let keys : string[] = Object.keys(this.variants[i]);
        this.variants[i] = {"variant": this.variants[i]["variant"], "count": this.variants[i][keys[0]]};
        i++;
      }
      this.variantsLoading = true;
      this.isLoading = this.variantsLoading || this.casesLoading;
      this.dataSourceVariants.data = this.variants;
      console.log(this.variants);
    })
  }

}
