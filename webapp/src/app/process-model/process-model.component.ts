import { Component, OnInit } from '@angular/core';
import { DomSanitizer, SafeResourceUrl, SafeUrl } from '@angular/platform-browser';
import { Pm4pyService } from '../pm4py-service.service';
import {Observable} from "rxjs";

@Component({
  selector: 'app-process-model',
  templateUrl: './process-model.component.html',
  styleUrls: ['./process-model.component.scss']
})
export class ProcessModelComponent implements OnInit {
  processModelBase64Original: string;
  processModelBase64Sanitized: SafeResourceUrl;
  pm4pyJson : JSON;

  constructor(private _sanitizer: DomSanitizer, private pm4pyService: Pm4pyService) {
    pm4pyService.getProcessSchema().subscribe(data => { this.pm4pyJson = data as JSON; this.processModelBase64Original = this.pm4pyJson["base64"]; this.processModelBase64Sanitized = this._sanitizer.bypassSecurityTrustResourceUrl('data:image/svg+xml;base64,' + this.processModelBase64Original); console.log(this.processModelBase64Sanitized); });
  }

  ngOnInit() {

  }

}
