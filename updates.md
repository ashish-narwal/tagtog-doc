---
layout: page
title: Updates
sidebar_link: true
id: updates
---

Here is the versioned list of all the new features, fixes, and other changes. [tagtog Cloud](https://www.tagtog.net) runs always on the latest version. If you are running **tagtog On-Premises**, make sure to [update to the latest version](on_premises_README.html) to make the most of your experience. Note that the versioning system (in particular the [minor version](https://semver.org)), tells you the time period when the update happened.

Have feedback? :heart: Report bugs and/or suggest improvements on our [:point_right:GitHub issues page:point_left:](https://github.com/tagtog/tagtog-doc/issues).

## 3.2018-W26.0 ⚽️

### Webhooks

<ul class="updates">
  <li class="new">You can now choose the new <code>tagtogID</code> (pseudo-)format in your <b>webhooks</b> to POST the updated document's id</li>
  <li class="new">You can now delete webhooks 😉</li>
  <li class="fix"><b>Webhooks</b> are now also triggered on new document uploads that have <i>no annotations</i></li>
  <li class="del">The formats <code>docJSON</code> and <code>PubAnnotation</code> were removed from the possible <b>webhooks</b>' payload. We might review this decision.</li>
</ul>

### More!

<ul class="updates">  
  <li class="new">API call to get a JSON map of the annotations legend, <i>anntasks ids → names</i>. For a sample call, check your project's <kbd>Downloads</kbd> page.</li>
  <li class="fix">Fixed a bug that prevented the training of ML models for entities that had associated dictionaries (specifically created through the interface).</li>
  <li class="doc">This new page of release notes was created 🤩</li>
</ul>