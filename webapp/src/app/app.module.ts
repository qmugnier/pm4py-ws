import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { FlexLayoutModule } from '@angular/flex-layout';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ProcessModelComponent } from './process-model/process-model.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';
import { HeaderComponent } from './header/header.component';
import { FiltersComponent } from './filters/filters.component';
import { FooterComponent } from './footer/footer.component';
import { MatSliderModule } from '@angular/material';
import { MatToolbarModule } from '@angular/material';
import { RouterModule, Routes } from '@angular/router';
import { StatisticsComponent } from './statistics/statistics.component';
import { CasesComponent } from './cases/cases.component';
import { SnaComponent } from './sna/sna.component';

const appRoutes: Routes = [
  { path: '', component: AppComponent },
  { path: 'sna', component: AppComponent },
  { path: 'cases', component: AppComponent },
  { path: 'statistics', component: AppComponent },
];



@NgModule({
  declarations: [
    AppComponent,
    ProcessModelComponent,
    HeaderComponent,
    FiltersComponent,
    FooterComponent,
    StatisticsComponent,
    CasesComponent,
    SnaComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatSliderModule,
    MatToolbarModule,
    FlexLayoutModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    )  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
