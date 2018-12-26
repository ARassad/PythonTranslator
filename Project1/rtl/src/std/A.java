/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package std;

/**
 *
 * @author Arkadi
 */
public class A extends __PyGenericObject{
    public __PyGenericObject __call__(__PyGenericObject a, __PyGenericObject b) throws Exception{
        __PyGenericObject a1 = new __PyInteger(100);
        __PyGenericObject a2 = new __PyFloat((float) 12);
        
        return a1.__add__(a2);
    }
}
