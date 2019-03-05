import { Component, OnInit } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
  selector: 'app-process-model',
  templateUrl: './process-model.component.html',
  styleUrls: ['./process-model.component.scss']
})
export class ProcessModelComponent implements OnInit {

  constructor(private _sanitizer: DomSanitizer) { }

  ngOnInit() {
  }

}
