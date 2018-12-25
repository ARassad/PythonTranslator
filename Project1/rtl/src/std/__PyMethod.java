/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package std;

import java.util.HashMap;

/**
 *
 * @author Arkadi
 */
public class __PyMethod extends __PyGenericObject{

    public __PyMethod() {
        super();
    }
    
    public __PyMethod(HashMap<String, __PyGenericObject> externalDir) {
        this();
        __dir__.clear();
        __dir__.putAll(externalDir);
    }
    
    public __PyGenericObject __call__() throws Exception {
        return this;
    }
}
