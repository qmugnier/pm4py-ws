import {Component, OnInit} from '@angular/core';
import {DomSanitizer, SafeResourceUrl, SafeUrl} from '@angular/platform-browser';
import {Pm4pyService} from '../pm4py-service.service';
import {HttpParams} from "@angular/common/http";

@Component({
  selector: 'app-process-model',
  templateUrl: './process-model.component.html',
  styleUrls: ['./process-model.component.scss'],
  host: {
    '(window:resize)': 'onResize($event)'
  }
})
export class ProcessModelComponent implements OnInit {
  processModelBase64Original: string;
  processModelBase64Sanitized: SafeResourceUrl;
  pm4pyJson: JSON;
  simplicity = 0.45;
  selectedSimplicity = 0.45;
  logSummaryJson: JSON;
  public thisVariantsNumber = 0;
  public thisCasesNumber = 0;
  public thisEventsNumber = 0;
  public ancestorVariantsNumber = 0;
  public ancestorCasesNumber = 0;
  public ancestorEventsNumber = 0;
  public ratioVariantsNumber = 100;
  public ratioCasesNumber = 100;
  public ratioEventsNumber = 100;
  decoration = 'freq';
  typeOfModel = 'dfg';
  sanitizer: DomSanitizer;
  pm4pyService: Pm4pyService;
  public isLoading: boolean;

  constructor(private _sanitizer: DomSanitizer, private pm4pyServ: Pm4pyService) {
    /**
     * Constructor
     */
    this.sanitizer = _sanitizer;
    this.pm4pyService = pm4pyServ;
    // calls the retrieval of the process schema from the service
    this.populateProcessSchema();
    this.getLogSummary();
  }

  public populateProcessSchema() {
    /**
     * Retrieves and shows the process schema
     */
    this.isLoading = true;
    let params: HttpParams = new HttpParams();
    params = params.set("simplicity", this.selectedSimplicity.toString());
    params = params.set("decoration", this.decoration);
    params = params.set("typeOfModel", this.typeOfModel);

    this.pm4pyService.getProcessSchema(params).subscribe(data => {
      this.pm4pyJson = data as JSON;
      this.processModelBase64Original = this.pm4pyJson["base64"];
      this.processModelBase64Sanitized = this.sanitizer.bypassSecurityTrustResourceUrl('data:image/svg+xml;base64,' + this.processModelBase64Original);
      this.setImageCorrectSize();
      this.isLoading = false;
    });
  }

  public getLogSummary() {
    /**
     * Retrieves the log summary and updates the visualization
     */
    let params: HttpParams = new HttpParams();

    this.pm4pyService.getLogSummary(params).subscribe(data => {
      this.logSummaryJson = data as JSON;
      this.thisVariantsNumber = this.logSummaryJson["this_variants_number"];
      this.thisCasesNumber = this.logSummaryJson["this_cases_number"];
      this.thisEventsNumber = this.logSummaryJson["this_events_number"];
      this.ancestorVariantsNumber = this.logSummaryJson["ancestor_variants_number"];
      this.ancestorCasesNumber = this.logSummaryJson["ancestor_cases_number"];
      this.ancestorEventsNumber = this.logSummaryJson["ancestor_events_number"];
      if (this.ancestorVariantsNumber > 0) {
        this.ratioVariantsNumber = this.thisVariantsNumber / this.ancestorVariantsNumber * 100.0;
        this.ratioCasesNumber = this.thisCasesNumber / this.ancestorCasesNumber * 100.0;
        this.ratioEventsNumber = this.thisEventsNumber / this.ancestorEventsNumber * 100.0;
      }
      else {
        this.ratioVariantsNumber = 100;
        this.ratioCasesNumber = 100;
        this.ratioEventsNumber = 100;
      }
    });
  }

  setImageCorrectSize() {
    /**
     * Sets the correct size of the image decribing the process schema
     */
    let targetHeight: number = (document.getElementById("container0").offsetHeight * 0.74);
    let targetWidth: number = (document.getElementById("container0").offsetWidth * 0.72);

    (<HTMLImageElement>document.getElementById("imageProcessModelImage")).height = targetHeight;
    (<HTMLImageElement>document.getElementById("imageProcessModelImage")).width = targetWidth;
  }

  ngOnInit() {
    /**
     * Method that is called at the initialization of the component
     */
  }

  onResize(event) {
    /**
     * Manages the resizing of a page
     */
    // sets the image size after the resizing
    this.setImageCorrectSize();
  }

  sliderIsChanged(event: any) {
    /**
     * Manages the change to the value selected in the slider
     */
    this.selectedSimplicity = event.value;
    // calls the retrieval of the process schema from the service
    this.populateProcessSchema();
  }

  decorationIsChanged(event: any) {
    /**
     * Manages the change of the type of decoration (frequency/performance)
     */
    this.decoration = event.value;
    // calls the retrieval of the process schema from the service
    this.populateProcessSchema();
  }

  typeOfModelIsChanged(event: any) {
    /**
     * Manages the change on the type of the model (discovery algorithm)
     */
    this.typeOfModel = event.value;
    // calls the retrieval of the process schema from the service
    this.populateProcessSchema();
  }

  mouseWheel(event: any) {
    if (event["deltaY"] < 0) {
      (<HTMLImageElement>document.getElementById("imageProcessModelImage")).height = (<HTMLImageElement>document.getElementById("imageProcessModelImage")).height * 1.1;
      (<HTMLImageElement>document.getElementById("imageProcessModelImage")).width = (<HTMLImageElement>document.getElementById("imageProcessModelImage")).width * 1.1;
    }
    else {
      (<HTMLImageElement>document.getElementById("imageProcessModelImage")).height = (<HTMLImageElement>document.getElementById("imageProcessModelImage")).height * 0.9;
      (<HTMLImageElement>document.getElementById("imageProcessModelImage")).width = (<HTMLImageElement>document.getElementById("imageProcessModelImage")).width * 0.9;
    }
  }

}
