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
import { MatProgressBarModule } from '@angular/material';
import { MatButtonModule } from '@angular/material';
import { MatFormFieldModule } from '@angular/material';
import { MatOptionModule } from '@angular/material';
import { MatSelectModule } from '@angular/material';
import { MatRadioModule } from '@angular/material';
import { MatListModule } from '@angular/material';
import { MatProgressSpinnerModule } from '@angular/material';
import { MatMenuModule } from '@angular/material';
import { MatIconModule } from '@angular/material';
import { MatTableModule } from '@angular/material';




import { RouterModule, Routes } from '@angular/router';
import { StatisticsComponent } from './statistics/statistics.component';
import { CasesComponent } from './cases/cases.component';
import { SnaComponent } from './sna/sna.component';
import { ProcessListComponent } from './process-list/process-list.component';
import { TransientComponent } from './transient/transient.component';

const appRoutes: Routes = [
  { path: 'process', component: AppComponent },
  { path: 'sna', component: AppComponent },
  { path: 'cases', component: AppComponent },
  { path: 'statistics', component: AppComponent },
  { path: 'logsList', component: AppComponent },
  { path: 'simulation', component: TransientComponent },
  { path: '**', redirectTo: 'logsList' }
];



@NgModule({
  declarations: [
    AppComponent,
    ProcessListComponent,
    HeaderComponent,
    FiltersComponent,
    FooterComponent,
    StatisticsComponent,
    CasesComponent,
    ProcessModelComponent,
    SnaComponent,
    TransientComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatSliderModule,
    MatToolbarModule,
    MatProgressBarModule,
    MatButtonModule,
    MatFormFieldModule,
    MatOptionModule,
    MatSelectModule,
    MatRadioModule,
    MatListModule,
    MatMenuModule,
    MatTableModule,
    MatIconModule,
    FlexLayoutModule,
    MatProgressSpinnerModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true, onSameUrlNavigation: 'reload' } // <-- debugging purposes only
    )  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
