import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PmodelComponent } from './pmodel/pmodel.component';
import { CasesComponent } from './cases/cases.component';

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
                path: 'cases',
                component: CasesComponent,
                data: {
                    title: 'CasesComponent'
                }
            }
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule],
})
export class RealWsRoutingModule { }
