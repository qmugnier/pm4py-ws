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
  styleUrls: ['./cases.component.scss'],
  host: {
    '(window:resize)': 'onResize($event)'
  }
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
  width : number = 1310;
  height : number = 170;


  constructor(private _sanitizer: DomSanitizer, private pm4pyServ: Pm4pyService) {
    /**
     * Constructor
     */
    this.sanitizer = _sanitizer;
    this.pm4pyService = pm4pyServ;
    this.variantsLoading = false;
    this.casesLoading = false;
    this.isLoading = false;

    //this.setTableSize();
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

  setTableSize() {
    /*console.log(screen.height);
    console.log(screen.width);
    var targetHeight = Math.floor(0.25 * screen.height) + "px";
    var targetWidth = Math.floor(0.25 * screen.width) + "px";
    let elem: HTMLElement = document.getElementById('tableVariants');

    elem.setAttribute("style", "height: "+targetHeight+"px; width: "+targetWidth+"px;");*/
    this.height = Math.floor(0.22 * window.innerHeight);
    this.width = Math.floor(0.968 * window.innerWidth);

    console.log(this.width);
    console.log(this.height);
  }

  onResize(event) {
    /**
     * Manages the resizing of a page
     */
    // sets the image size after the resizing
    this.setTableSize();
  }

  ngAfterViewInit() {
    this.setTableSize();
  }

}
