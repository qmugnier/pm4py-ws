import { TestBed } from '@angular/core/testing';

import { Pm4pyServiceService } from './pm4py-service.service';

describe('Pm4pyServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: Pm4pyServiceService = TestBed.get(Pm4pyServiceService);
    expect(service).toBeTruthy();
  });
});
