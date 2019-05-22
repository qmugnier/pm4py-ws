import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PmodelComponent } from './pmodel/pmodel.component';

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
            }
        ]
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule],
})
export class RealWsRoutingModule { }
