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
    this.sanitizer = _sanitizer;
    this.pm4pyService = pm4pyServ;
    this.populateSNA();
  }

  public populateSNA() {
    let snaPlainUrl : string = this.pm4pyService.getServicePath() + "getSNA";

    this.snaContent = this.sanitizer.bypassSecurityTrustResourceUrl(snaPlainUrl);

    console.log(snaPlainUrl);

    //this.doResizing();
  }

  ngOnInit() {
  }

  onResize(event) {
    event.target.innerWidth; // window width
    this.doResizing();
  }

  doResizing() {
    let targetHeight: number = (document.getElementById("container0").offsetHeight * 0.74);

    console.log("DIVSNA");
    console.log(document.getElementById("divSna"));

    document.getElementById("divSna").style.height = ""+targetHeight+"px";
  }

  ngAfterViewInit() {
    this.doResizing();
  }

  changeSelectedArcValue(event) {
    this.selectedArcsThreshold = event.value;
  }

  metricChanged(event) {
    this.metric = event.value;
  }
}
