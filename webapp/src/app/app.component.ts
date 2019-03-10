import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'webapp';
  process_provided : boolean = false;
  router : Router;
  route : ActivatedRoute;

  constructor(private _router: Router, private _route : ActivatedRoute) {
    this.router = _router;
    this.route = _route;
    console.log("ROUTER URL");
    console.log(_router.url);
  }

  ngOnInit() {
    let url : string = window.location.href;
    if (url.split("process=").length > 1) {
      this.process_provided = true;
      let process : string = url.split("process=")[1].split("&")[0];
      localStorage.setItem("process", process);
    }
    else {
      this.process_provided = false;
      localStorage.setItem("process", "receipt");
    }
  }
}
