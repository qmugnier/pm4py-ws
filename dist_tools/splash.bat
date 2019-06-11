@echo off &setlocal

:: these variables will be expanded in the HTA code
set /a sec = 13
set /a width = 800
set /a height = 533
set "fullname=%cd%\splash.jpg"


set "splash=%temp%\tmp.hta"
:: all lines beginning with min. 6 spaces are redirected into the HTA file
>"%splash%" (type "%~f0"|findstr /bc:"      ")
mshta "%splash%"
del "%splash%"

echo Done.
pause
goto :eof
:: End Of Batch

      <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "xhtml1-transitional.dtd">
      <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
          <title>SPLASH</title>

          <hta:application
           id="oHTA"
           applicationname="myApp"
           border="thin"
           borderstyle="normal"
           caption="no"
           contextmenu="yes"
           icon=""
           innerborder="no"
           maximizebutton="no"
           minimizebutton="no"
           navigable="no"
           scroll="no"
           scrollflat="no"
           selection="no"
           showintaskbar="no"
           singleinstance="yes"
           sysmenu="no"
           version="1.0"
           windowstate="normal"
          />

          <style type="text/css">
            body      {margin:0px 0px 0px 0px;}
          </style>

          <script type="text/jscript">
            /* <![CDATA[ */
            
            var oWSH=new ActiveXObject("WScript.Shell");
            var i=parseInt(oWSH.ExpandEnvironmentStrings("%sec%"))*1000;
            var w=parseInt(oWSH.ExpandEnvironmentStrings("%width%"));
            var h=parseInt(oWSH.ExpandEnvironmentStrings("%height%"));
            var s=oWSH.ExpandEnvironmentStrings("%fullname%");
            window.resizeTo(w, h);
            window.moveTo(screen.width/2-w/2, screen.height/2-h/2);


            function start() {
              image.src = s;
              image.height = h;
              image.width = w;
              setTimeout('closing()', i);
            }

            function closing() {
              window.close();
            }
            /* ]]> */
          </script>

        </head>
        <body onload="start()">
          <img id="image" src="" alt="" height="0" width="0" /> 
        </body>
      </html>
