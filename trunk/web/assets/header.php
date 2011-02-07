
<!--- 
File: header.php 
Purpose: Website header information 
Submitted-By: Thomas Boxley
Copyright 2011 Matt Arnold

To the extent that this file is copyrightable 
it is open content you are free to use it in any way
as long as you give credit to the Submitter, and
copyright holder      
--->
<!DOCTYPE html>
<html>
<head>
<title>Hephaestus Workshop</title>
<meta charset="UTF-8">
<style type='text/css'>
body {
	background-color:#bcbcbc;
	font-family: Verdana, Arial, Helvetica, sans-serif;
	}

a:link,a:visited,a:active {
	color:#4B6983;
	text-decoration:underline;
	}
	
a:hover {
	color:#333333;
	text-decoration:none;
	}
	
.content {
	background-color:#ffffff;
	border:2px solid #666666;
	margin-left:auto;
	margin-right:auto;
	width:900px;
	border-radius:10px;
	-moz-border-radius:10px;
	}
	
.header {
	background-image:url('assets/background.png');
	border-bottom:2px solid #666666;
	border-radius:6px;
	-moz-border-radius:6px;
	padding:15px;
	text-shadow:1px 1px 1px #000000;
	color:#ffffff;
	}
	
.header a {
	font-size:36px;
	text-decoration:none;
	color:#ffffff;
	}
	
p {
	text-align:justify;
	padding:10px;
	line-height: 25px;
	font-size:14px;
	}
	
ul.navigation {
	margin-top:0px;
	list-style: none;
	width:900px;
	height:30px;
	padding:0;
	}
	
ul.navigation li {
	float: right;
	line-height:29px;
	height:29px;
	background-color:#ececec;
	border-left:1px solid #666666;
	border-bottom:1px solid #666666;
	padding:5px 10px 5px 10px;
	}
	
ul.navigation li:hover {
	cursor:hand;
	background-color:#f5f5f5;
	}
	
ul.navigation li a {
	display: block;
	color:#4B6983;
	font-size:14px;
	}
	
ul.navigation li a:hover {
	text-decoration:underline;
	}
	
.description {
	float:right;
	font-size:15px;
	margin-top:15px;
	}
	
.title {
	font-size:25px;
	float:left;
	display:block;
	margin-top:-40px;
	padding-left:10px;
	text-decoration:underline;
	}
	
.footer {
	font-size:9px;
	border-bottom:1px solid #666666;
	border-right:1px solid #666666;
	border-left:1px solid #666666;
	width:400px;
	margin-left:auto;
	margin-right:auto;
	margin-top:0px;
	background-color:#F5F5F5;
	padding:2px;
	text-align:center;
	border-bottom-left-radius:5px; 
	-moz-border-radius-bottomleft:5px;
	border-bottom-right-radius:5px; 
	-moz-border-radius-bottomleft:5px;
	}
	
.rightmost {
	margin-right:20px;
	border-bottom-right-radius:10px;
	-moz-border-radius-bottomright:10px;
	border-right:1px solid #666666;
	}
	
.leftmost {
	border-bottom-left-radius:10px;
	-moz-border-radius-bottomleft:10px;
	}
	
</style>
</head>
<!-- Don't be alarmed. Just some PHP just to make the Valid URL work -->
<?php
function curPageURL() {
 $pageURL = 'http';
 if ($_SERVER["HTTPS"] == "on") {$pageURL .= "s";}
 $pageURL .= "://";
 if ($_SERVER["SERVER_PORT"] != "80") {
  $pageURL .= $_SERVER["SERVER_NAME"].":".$_SERVER["SERVER_PORT"].$_SERVER["REQUEST_URI"];
 } else {
  $pageURL .= $_SERVER["SERVER_NAME"].$_SERVER["REQUEST_URI"];
 }
 return $pageURL;
}
?>
<!-- End teh php -->

<body>
<div class='content'>
<div class='header'>
<a href='index.php'>Hephaestus Workshop</a>
<span class='description'>Accessibility tools for </span>
</div>
<!--
READ THIS MARNOLD
List elements are in reverse order because of float:right in CSS.
Too lazy to fix. It works anyways 
-->
<ul class='navigation'>
<li	class='rightmost'><a href='download.php'>Download</a></li>
<li><a href='about.php'>About</a></li>
<li><a href='other.php'>Other</a></li>
<li class='leftmost'><a href='index.php'>Home</a></li>
</ul>
