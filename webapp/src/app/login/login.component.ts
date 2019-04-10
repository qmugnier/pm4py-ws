import { Component, OnInit } from '@angular/core';
import {DomSanitizer} from "@angular/platform-browser";
import {Pm4pyService} from "../pm4py-service.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  username : string;
  password : string;
  sanitizer: DomSanitizer;
  pm4pyService: Pm4pyService;
  router: Router;

  constructor(private _route: Router, private _sanitizer: DomSanitizer, private pm4pyServ: Pm4pyService) {
    this.pm4pyService = pm4pyServ;
    this.sanitizer = _sanitizer;
    this.router = _route;

    localStorage.removeItem("sessionId");

    this.username = "";
    this.password = "";
  }

  ngOnInit() {
  }

  login() {
    this.pm4pyService.loginService(this.username, this.password).subscribe(data => {
      let resultJson : JSON = data as JSON;
      console.log(resultJson);

      if (resultJson["status"] == "OK") {
        localStorage.setItem("sessionId", resultJson["sessionId"]);
        this.router.navigateByUrl('/logsList');
      }
      else {
        alert("Login failed! Try again");
      }
    });
  }

}
