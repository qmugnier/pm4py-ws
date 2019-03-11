import {Component, OnInit} from '@angular/core';
import {Router} from "@angular/router";

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {
  public processProvided: boolean;
  router: Router;


  constructor(private _route: Router) {
    this.router = _route;
    this.router.events.subscribe((val) => {
      let process_name: string = localStorage.getItem("process");
      if (process_name != null) {
        if (this.router.url === "/logsList") {
          this.processProvided = false;
        }
        else {
          this.processProvided = true;
        }
      }
      else {
        this.processProvided = false;
      }
    });
  }

  ngOnInit() {
    this.processProvided = false;
    let process_name: string = localStorage.getItem("process");
    if (process_name != null) {
      this.processProvided = true;
    }
    else {
      this.processProvided = false;
    }
  }

  public resetProcessProvided(value: boolean) {
    this.processProvided = value;
  }

}
