import { Component, Output, EventEmitter, OnDestroy, OnInit, AfterViewInit } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';
import { LayoutService } from '../services/layout.service';
import { Subscription } from 'rxjs';
import { ConfigService } from '../services/config.service';
import {AuthenticationServiceService} from '../../authentication-service.service';
import {Router, RoutesRecognized} from '@angular/router';

@Component({
  selector: "app-navbar",
  templateUrl: "./navbar.component.html",
  styleUrls: ["./navbar.component.scss"]
})
export class NavbarComponent implements OnInit, AfterViewInit, OnDestroy {
  currentLang = "en";
  toggleClass = "ft-maximize";
  placement = "bottom-right";
  public isCollapsed = true;
  layoutSub: Subscription;
  @Output()
  toggleHideSidebar = new EventEmitter<Object>();

  public config: any = {};

  public sessionId : string;
  public userId : string;
  public isNotLogin : boolean;
  public enableDownload : boolean;
  public enableUpload : boolean;
  public thisProcess : string;

  constructor(public translate: TranslateService, private layoutService: LayoutService, private configService:ConfigService, private authService: AuthenticationServiceService, private _route : Router) {
    const browserLang: string = translate.getBrowserLang();
    translate.use(browserLang.match(/en|es|pt|de/) ? browserLang : "en");

    this.layoutSub = layoutService.changeEmitted$.subscribe(
      direction => {
        const dir = direction.direction;
        if (dir === "rtl") {
          this.placement = "bottom-left";
        } else if (dir === "ltr") {
          this.placement = "bottom-right";
        }
      });

    this.sessionId = null;
    this.userId = null;
    this.isNotLogin = false;
    this.enableDownload = false;
    this.enableUpload = false;
    this.thisProcess = null;

    this._route.events.subscribe((next) => {
      if (next instanceof RoutesRecognized) {
        if (next.url.startsWith("/real-ws/pmodel") || next.url.startsWith("/real-ws/plist")) {
          this.authService.checkAuthentication().subscribe(data => {
            this.sessionId = data.sessionId;
            this.userId = data.userId;
            this.isNotLogin = data.isNotLogin;
            this.enableDownload = data.enableDownload;
            this.enableUpload = data.enableUpload;
            this.thisProcess = localStorage.getItem("process");
          });
        }
      }
    });
  }

  ngOnInit() {
    this.config = this.configService.templateConf;
  }

  ngAfterViewInit() {
    if(this.config.layout.dir) {
      setTimeout(() => {
        const dir = this.config.layout.dir;
        if (dir === "rtl") {
          this.placement = "bottom-left";
        } else if (dir === "ltr") {
          this.placement = "bottom-right";
        }
      }, 0);
     
    }
  }

  ngOnDestroy() {
    if (this.layoutSub) {
      this.layoutSub.unsubscribe();
    }
  }

  ChangeLanguage(language: string) {
    this.translate.use(language);
  }

  ToggleClass() {
    if (this.toggleClass === "ft-maximize") {
      this.toggleClass = "ft-minimize";
    } else {
      this.toggleClass = "ft-maximize";
    }
  }

  toggleNotificationSidebar() {
    this.layoutService.emitNotiSidebarChange(true);
  }

  toggleSidebar() {
    const appSidebar = document.getElementsByClassName("app-sidebar")[0];
    if (appSidebar.classList.contains("hide-sidebar")) {
      this.toggleHideSidebar.emit(false);
    } else {
      this.toggleHideSidebar.emit(true);
    }
  }

  logout() {
    this.authService.doLogout();
  }

  goToHome() {
    this._route.navigateByUrl("/real-ws/plist");
  }
}
