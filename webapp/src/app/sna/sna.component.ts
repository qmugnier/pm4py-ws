import { Component, OnInit } from '@angular/core';
import {HttpParams} from "@angular/common/http";
import {Pm4pyService} from "../pm4py-service.service";
import {DomSanitizer, SafeHtml, SafeResourceUrl, SafeUrl} from "@angular/platform-browser";

@Component({
  selector: 'app-sna',
  templateUrl: './sna.component.html',
  styleUrls: ['./sna.component.scss'],
  host: {
    '(window:resize)': 'onResize($event)'
  }
})
export class SnaComponent implements OnInit {
  public snaContent : SafeResourceUrl;
  sanitizer: DomSanitizer;
  pm4pyService: Pm4pyService;
  arcsThreshold : number = 0.0;
  selectedArcsThreshold : number = 0.0;
  metric : string = "handover";

  constructor(private _sanitizer: DomSanitizer, private pm4pyServ: Pm4pyService) {
    /**
     * Constructor
     */
    this.sanitizer = _sanitizer;
    this.pm4pyService = pm4pyServ;
    // gets the SNA representation
    this.populateSNA();
  }

  public populateSNA() {
    /**
     * Gets the SNA representation and includes it as an IFrame object
     */
    let process : string = localStorage.getItem("process");
    let snaPlainUrl : string = this.pm4pyService.getServicePath() + "getSNA?process="+process+"&metric="+this.metric+"&threshold="+this.selectedArcsThreshold;

    this.snaContent = this.sanitizer.bypassSecurityTrustResourceUrl(snaPlainUrl);

    console.log(snaPlainUrl);

    //this.doResizing();
  }

  ngOnInit() {
    /**
     * Method that is called at the initialization of the component
     */
  }

  onResize(event) {
    /**
     * Manages the resizing of the view
     */
    this.doResizing();
  }

  doResizing() {
    /**
     * Do the resizing of the div to the target height
     */
    let targetHeight: number = (document.getElementById("container0").offsetHeight * 0.74);

    document.getElementById("divSna").style.height = ""+targetHeight+"px";
  }

  ngAfterViewInit() {
    /**
     * Method that is called after finishing rendering the page
     */
    this.doResizing();
  }

  changeSelectedArcValue(event) {
    /**
     * Manages the change on the selected arc value
     */
    this.selectedArcsThreshold = event.value;
    // calls again the SNA representation
    this.populateSNA();
  }

  metricChanged(event) {
    /**
     * Manages the change on the selected metric
     */
    this.metric = event.value;
    // calls again the SNA representation
    this.populateSNA();
  }
}
