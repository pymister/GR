import Vue from 'vue'
import Router from 'vue-router'

//导入让用户访问的组件
import  Home from '../components/Home'

Vue.use(Router);

export default new Router({
  mode:'history',
  routes:[
    //路由列表
    {
      name:'Home',
      path:'/',
      component:Home
    },

  ]
})
