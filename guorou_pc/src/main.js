// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

import router from './router/index'

Vue.config.productionTip = false;

//开发配置文件
import settings from "./settings";
import "../static/css/reset.css";
Vue.prototype.$settings = settings;

import axios from 'axios'; // 从node_modules目录中导入包
// 允许ajax发送请求时附带cookie
axios.defaults.withCredentials = true;

Vue.prototype.$axios = axios; // 把对象挂载vue中

//elementUI导入
import ElementUI from 'element-ui';
// import 'element-ui/lib/theme-chalk/index.css'
//调用插件
Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});
