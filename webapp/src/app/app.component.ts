import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'webapp';
  public process_provided : boolean = false;
  public process_name : string;
  router : Router;
  route : ActivatedRoute;

  constructor(private _router: Router, private _route : ActivatedRoute) {
    /**
     * Constructor
     */
    this.router = _router;
    this.route = _route;
    this.router.events.subscribe((val) => {
      let process_name: string = localStorage.getItem("process");
      if (process_name != null) {
        if (this.router.url === "/logsList") {
          this.process_provided = false;
        }
        else {
          this.process_provided = true;
        }
      }
      else {
        this.process_provided = false;
      }
    });
  }

  ngOnInit() {
    /**
     * Method that is called on initialization of the app
     */
    let url : string = window.location.href;
    if (url.split("process=").length > 1) {
      // the process has been provided through URL
      this.process_provided = true;
      this.process_name = url.split("process=")[1].split("&")[0];
      localStorage.setItem("process", this.process_name);
    }
    else if (localStorage.getItem("process") != null) {
      // the process has been provided by local storage
      this.process_provided = true;
      this.process_name = localStorage.getItem("process");
    }
    else {
      // no information about the process has been provided
      this.process_provided = false;
    }
  }
}
