OpenSSL
----

```
ruby -ropenssl -ve 'p OpenSSL::SSL::SSLContext.new.ciphers'
```

Mixin
----

```
module Post
  @@year = 2011

  def title
    "#{@title} (#{@@year})"
  end
end

class Article
  include Post # <- Include the module Post

  def initialize(title)
    @title = title
  end
end

Article.new("I'm a Rubyist").title # => "I'm a Rubyist (2011)"
```