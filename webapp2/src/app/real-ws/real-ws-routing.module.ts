import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PmodelComponent } from './pmodel/pmodel.component';
import { CasesComponent } from './cases/cases.component';
import { StatisticsComponent } from './statistics/statistics.component';
import { LoginComponentComponent } from './login-component/login-component.component';
import { PlistComponent } from './plist/plist.component';

const routes: Routes = [
    {
        path: '',
        children: [
            {
                path: 'pmodel',
                component: PmodelComponent,
                data: {
                    title: 'PmodelComponent'
                }
            },
            {
                path: 'pmodel2',
                component: PmodelComponent,
                data: {
                    title: 'PmodelComponent'
                }
            },
            {
                path: 'cases',
                component: CasesComponent,
                data: {
                    title: 'CasesComponent'
                }
            },
            {
                path: 'statistics',
                component: StatisticsComponent,
                data: {
                    title: 'StatisticsComponent'
                }
            },
            {
                path: 'login',
                component: LoginComponentComponent,
                data: {
                    title: 'LoginComponent'
                }
            },
            {
                path: 'plist',
                component: PlistComponent,
                data: {
                    title: 'ProcessList'
                }
            },
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule],
})
export class RealWsRoutingModule { }
