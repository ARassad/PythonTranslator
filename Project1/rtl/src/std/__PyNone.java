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
public class __PyNone extends __PyGenericObject{
    
    
    public __PyGenericObject __str__(){
        return  new __PyString("None");
    }
}