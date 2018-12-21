/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package std;

import java.util.LinkedList;
import sun.reflect.generics.reflectiveObjects.NotImplementedException;

/**
 *
 * @author Arkadi
 */
public class __PyList extends __PyGenericObject {

    public __PyList() {
        super();
        __list__ = new LinkedList<>();
    }
    
    //Type cast
    public __PyGenericObject __str__() throws Exception{
        String res = "[";
        int l = __list__.size();
        for(int i = 0; i < l; i++){
            res = res + this.__list__.get(i).__str__();
            if(i != l - 1)
                res = res + ',';
        }
        res = res + ']';
        return new __PyString(res);
    }
    
    public __PyGenericObject __list__(){
       return this;
    }
    
    public __PyGenericObject __bool__() {
       return new __PyInteger(this.__list__.size() != 0);
    }
    
    // List 
    public __PyGenericObject __contains__(__PyGenericObject value) {
        boolean found = false;
        int l = this.__list__.size();
        int i = 0;
        while(!found && i < l){
            try {
                found = this.__list__.get(i).__eq__(value).__integer__ != 0;
            } catch (Exception e) {
                
            }
        }
        return new __PyInteger(found);
    }
    
    public __PyGenericObject __delitem__(__PyGenericObject index) {
        if(!(index instanceof __PyInteger))
            throw new ArrayIndexOutOfBoundsException("Index must be int object");
        
        return this.__list__.remove(index.__integer__);
    }
    
    public __PyGenericObject __getitem__(__PyGenericObject index) {
        if(!(index instanceof __PyInteger))
            throw new ArrayIndexOutOfBoundsException("Index must be int object");
        int ind = index.__integer__;
        if(ind < 0)
            ind = this.__list__.size() - ind;
        return this.__list__.get(ind);
    }
    
    public __PyGenericObject append(__PyGenericObject value) {
        this.__list__.add(value);
        return this;
    }
    
    public __PyGenericObject index(__PyGenericObject value) {
        boolean found = false;
        int l = this.__list__.size();
        int i = 0;
        int index = -1;
        while(!found && i < l){
            try {
                found = this.__list__.get(i).__eq__(value).__integer__ != 0;
                if(found)
                    index = i;
            } catch (Exception e) {
                
            }
        }
        return new __PyInteger(index);
    }
 
    public __PyGenericObject remove(__PyGenericObject value) throws Exception{
       __PyGenericObject index = this.index(value);
       if(index.__integer__ == -1)
           throw new Exception("Value not in list");
       return this.__delitem__(index);
    }
    
    public __PyGenericObject extend(__PyGenericObject list) throws Exception {
        if(!(list instanceof __PyList))
            throw new Exception("Can extend only by list object");
        __PyList res = new __PyList();
        res.__list__.addAll(this.__list__);
        res.__list__.addAll(list.__list__);
        return res;
    }
    
    public __PyGenericObject __replaceitem(__PyGenericObject index, __PyGenericObject value) throws NotImplementedException{
        if(!(index instanceof __PyInteger))
            throw new ArrayIndexOutOfBoundsException("Index must be int object");
        int ind = index.__integer__;
        if(ind < 0)
            ind = this.__list__.size() - ind;
        __PyGenericObject var = this.__list__.remove(ind);
        this.__list__.add(ind, value);
        return var;
    }
    
    public __PyGenericObject insert(__PyGenericObject index, __PyGenericObject value) throws NotImplementedException{
        if(!(index instanceof __PyInteger))
            throw new ArrayIndexOutOfBoundsException("Index must be int object");
        int ind = index.__integer__;
        if(ind < 0)
            ind = this.__list__.size() - ind;
        this.__list__.add(ind, value);
        return this;
    }
    
    public __PyGenericObject clear() throws NotImplementedException{
        this.__list__.clear();
        return this;
    }
    
    public __PyGenericObject sort() throws Exception{
        __PyList res = new __PyList();
        
        int l = this.__list__.size();
        int num = 0;
        __PyGenericObject tmp;
        for(int i = 0; i < l; i++){
            tmp = this.__list__.get(i);
            int j = 0;
            while(true){
                if(j == num){
                    res.__list__.add(tmp);
                    num++;
                    break;
                }else{
                    if(res.__list__.get(j).__gt__(tmp).__integer__ == 0){
                        res.__list__.add(j, tmp);
                        num++;
                        break;
                    }
                    j++;
                }
            }
        }
        return res;
    }
    
    public __PyGenericObject __len__() throws NotImplementedException{
        return new __PyInteger(this.__list__.size());
    }
    
    public __PyGenericObject __add__(__PyGenericObject value) throws Exception {
        return this.extend(value);
    }
    
    public __PyGenericObject __mul__(__PyGenericObject value) throws Exception {
        if(!(value instanceof __PyInteger))
            throw new ArrayIndexOutOfBoundsException("Can multiply only by int object");
        
        __PyGenericObject res = this;
        for(int i = 1; i < value.__integer__; i++){
            res = res.extend(this);
        }
        return res;
    }
    
    // Equal
    public __PyGenericObject __lt__(__PyGenericObject value) throws Exception {
        if(!(value instanceof __PyList))
            throw new Exception("Can equal only with list object");
        
        int l1 = this.__list__.size();
        int l2 = value.__list__.size();
        
        if(l1 != l2){
            if(l1 < l2)
                return new __PyInteger(true);
            return new __PyInteger(false);
        }
            
        
        for(int i = 0; i < l1; i++){
            if(this.__list__.get(i).__lt__(value.__list__.get(i)).__integer__ == 0)
                return new __PyInteger(false);
        }
        return new __PyInteger(true);
    }
    
    public __PyGenericObject __le__(__PyGenericObject value) throws Exception {
        if(this.__lt__(value).__integer__ == 1)
            return new __PyInteger(true);
        if (this.__eq__(value).__integer__ == 1)
            return new __PyInteger(true);
        return new __PyInteger(false);
    }
    
    public __PyGenericObject __eq__(__PyGenericObject value) throws Exception  {
        if(!(value instanceof __PyList))
            throw new Exception("Can equal only with list object");
        
        int l1 = this.__list__.size();
        int l2 = value.__list__.size();
        
        if(l1 != l2)
            return new __PyInteger(false);
        
        for(int i = 0; i < l1; i++){
            if(this.__list__.get(i).__eq__(value.__list__.get(i)).__integer__ == 0)
                return new __PyInteger(false);
        }
        return new __PyInteger(true);
    }
    
    public __PyGenericObject __ne__(__PyGenericObject value) throws Exception {
        return new __PyInteger(this.__eq__(value).__integer__ != 1);
    }
    
    public __PyGenericObject __gt__(__PyGenericObject value) throws Exception {
        return new __PyInteger(this.__le__(value).__integer__ != 1);
    }
    
    public __PyGenericObject __ge__(__PyGenericObject value) throws Exception {
        return new __PyInteger(this.__lt__(value).__integer__ != 1);
    }
}
