CREATE DATABASE IF NOT EXISTS tiktok3r2;
use tiktok3r2;
CREATE TABLE `tiktoker` (
  `id` int(11) NOT NULL,
  `uid` mediumtext COLLATE utf8_bin DEFAULT NULL,
  `time` mediumtext COLLATE utf8_bin DEFAULT NULL,
  `hide` int(11) NOT NULL DEFAULT 0,
  `delete` int(11) NOT NULL DEFAULT 0,
  `addedby` mediumtext COLLATE utf8_bin DEFAULT NULL,
  `type` mediumtext COLLATE utf8_bin DEFAULT NULL,
  `name` mediumtext COLLATE utf8_bin DEFAULT NULL,
  `comments` longtext COLLATE utf8_bin DEFAULT NULL,
  `cover` longtext COLLATE utf8_bin DEFAULT NULL,
  `likes` longtext COLLATE utf8_bin DEFAULT NULL,
  `shares` longtext COLLATE utf8_bin DEFAULT NULL,
  `vid_id` longtext COLLATE utf8_bin DEFAULT NULL,
  `views` longtext COLLATE utf8_bin DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

ALTER TABLE `tiktoker`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `tiktoker`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=0;
