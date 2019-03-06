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
  simplicity = 0.6;
  selectedSimplicity = 0.6;
  sanitizer: DomSanitizer;
  pm4pyService: Pm4pyService;

  constructor(private _sanitizer: DomSanitizer, private pm4pyServ: Pm4pyService) {
    this.sanitizer = _sanitizer;
    this.pm4pyService = pm4pyServ;
    this.populateProcessSchema();
  }

  public populateProcessSchema() {
    let params: HttpParams = new HttpParams();
    params = params.set("simplicity", this.selectedSimplicity.toString());

    this.pm4pyService.getProcessSchema(params).subscribe(data => {
      this.pm4pyJson = data as JSON;
      this.processModelBase64Original = this.pm4pyJson["base64"];
      this.processModelBase64Sanitized = this.sanitizer.bypassSecurityTrustResourceUrl('data:image/svg+xml;base64,' + this.processModelBase64Original);
      this.setImageCorrectSize();
    });
  }

  setImageCorrectSize() {
    let targetHeight : number = (document.getElementById("container0").offsetHeight * 0.74);

    (<HTMLImageElement>document.getElementById("imageProcessModelImage")).height = targetHeight;
  }

  ngOnInit() {

  }

  onResize(event){
    event.target.innerWidth; // window width
    this.setImageCorrectSize();
  }

  sthingChanged(event: any) {
    this.selectedSimplicity = event.value;
  }

}
