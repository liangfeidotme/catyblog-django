catyblog
========

系统介绍
-------------
catyblog是一个基于Django的个人博客系统。前端框架使用bootstrap。
后台管理系统暂时使用Django的提供的admin应用。

主要功能
--------------

* 博文采用markdown格式
* 文章分类
* 文章归档
* 标签索引


TODO
---------------

* 博客后台Dashboard
* 搜索功能
* 抽取摘要
* 抽取关键词

使用catyblog的网站
-------------

* [Zealous Carrier](http://www.liangfeizc.com)


Trouble Shooting
----------------


- 代码更新后，启动uWSGI时出现 *unbind() Permission Denied* 的错误

  要确保catyblog目录的所有者为www-data:www-data而不是root:root
      sudo chown -R www-data:www-data catyblog

- 代码更新后，出现 *Server Error (500)*

  这时候要把Debug选项打开，查看是不是代码有bug

