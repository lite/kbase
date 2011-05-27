rake aborted
----

> You have already activated rake 0.9.0, but your Gemfile requires rake 0.8.7. Consider using bundle exec

```
gem uninstall rake -v 0.9
Gemfile: gem 'rake', '~> 0.8.7'
bundle update   

bundle exec rake db:migrate
```


