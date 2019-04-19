// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.

export const environment = {
  production: false,
  webServicePath: "http://localhost:5000/",
  enableUpload: true,
  enableDownload: true,
  enableLogin: true,
  loginTextHint: 'Username: admin Password: admin will give you full access to the system. Username: user1 Password: user1 will give you access to the running-example log along with the possibility to download the running-example. Username: user2 Password: user2 will give you access to the receipt log but without the possibility to download the log.'
};

/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.
