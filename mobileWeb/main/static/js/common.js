var COMMON = COMMON || {};

(function(common, $){
    $.extend(common,{
        //공백 여부 
        isEmpty : function(val){
            if(val == null || val.length == 0){
                return true
            }
            return false
        },
        //두 값이 같은지
        isSame : function(val1, val2){
            if(val1 != val2){
                return false
            }
            return true
        },
        getCookie : function(){
            var val = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)')
            return val ? val[2] : null;
        },
        //쿠키 저장
        setCookie : function(key, val, exp){
            var date = new Date()
            date.setTime(date.getTime() + exp*24*60*60*1000)
            document.cookie = key + '=' + val + ';expires' + date.toUTCString()
        },
        //쿠키 삭제
        deleteCookie : function(key){
            document.cookie = key + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
        },
    })
}(COMMON, $))