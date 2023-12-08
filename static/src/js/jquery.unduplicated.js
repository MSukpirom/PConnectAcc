(function($){
    // setbackground คือชื่อของ plugin ที่เราต้องการ ในที่นี้ ใช้ว่า  setbackground
    $.fn.unduplicated = function( options ) { // กำหนดให้ plugin ของเราสามารถ รับค่าเพิ่มเติมได้ มี options
       
        // ส่วนนี้ สำหรับกำหนดค่าเริ่มต้น
        var defaults={ 
            initialVal:null
        };
       
        // ส่วนสำหรับ  เป็นต้วแปร รับค่า options หากมี หรือใช้ค่าเริ่มต้น ถ้ากำหนด
        var settings = $.extend( {}, defaults, options );
 
        var arrSelectVal=[];
        var optionsObj = this.find("option");
 
        $(this).on("change",function(){
            arrSelectVal=[];
            var indexThis = $(".css_unduplicated").index(this);
            $(".css_unduplicated").each(function(i,k){      
                var optionHtml="";
                var prevObj = $(".css_unduplicated:lt("+i+")").length;
                var prevVal =   $(".css_unduplicated:eq("+(i-1)+")").val();
                if(prevObj>0){
                    arrSelectVal.push(prevVal);
                }
                if(i>0 && i!=indexThis && i>indexThis){   
                    $.each(optionsObj,function(s,html){             
                        if(arrSelectVal.indexOf($(html).val())==-1){
                            optionHtml+=html.outerHTML;                     
                        }
                    });
                }
                if(optionHtml!=""){
                    $(this).html(optionHtml);
                }
            });
        });              
        /// คืนค่ากลับ การทำงานของ plugin
        return this.each(function(j,k) {
            $(this).addClass("css_unduplicated");
            var optionHtml="";
            var prevObj = $(".css_unduplicated:lt("+j+")").length;
            var prevVal =   $(".css_unduplicated:eq("+(j-1)+")").val();
            if(prevObj>0){
                arrSelectVal.push(prevVal);
            }
            if(j>0){ 
                $.each(optionsObj,function(s,html){             
                    if(arrSelectVal.indexOf($(html).val())==-1){
                        optionHtml+=html.outerHTML;                     
                    }
                });
            }
            if(optionHtml!=""){
                $(this).html(optionHtml);
            }
             if(settings.initialVal!=null){
                 var setVal = settings.initialVal[j];
                 $(this).val(setVal);
             }          
        });   
    };
  
})(jQuery);