var COMMON = COMMON || {};

(function(common, $){
    $.extend(common,{
        isEmpty : function(val){
            if(val == null || val.length == 0){
                return true
            }
            return false
        },
        isSame : function(val1, val2){
            if(val1 != val2){
                return false
            }
            return true
        }
    })
}(COMMON, $))