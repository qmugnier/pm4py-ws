import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  public processProvided : boolean;


  constructor() { }

  ngOnInit() {
    this.processProvided = false;
    let process_name : string = localStorage.getItem("process");
    if (process_name != null) {
      this.processProvided = true;
    }
  }

}
