require 'nokogiri' 
require 'open-uri'
require 'net/http'
require 'ruby-debug'

ROOT_URI = 'http://coderstore.info/'
# $links =  {}
$links =  []

def spider_links(uri)
  doc = Nokogiri::HTML(open(uri))
  # <a href="BashCommandLineEditing/">BashCommandLineEditing/</a>
  doc.xpath('//pre/a').each do | link |
    c_uri = uri + link["href"]
    if not (c_uri =~ /iPhone/) and c_uri =~ /(mov|m4v)$/
      filename = File.basename(c_uri)
      puts "#{filename}: #{c_uri}" 
      # $links[filename] = c_uri
      $links.push(c_uri)
    else 
      if not (c_uri =~ /C=[A-Z];O=[A-Z]$/) and c_uri =~ /[\w_]+\/$/ 
        #puts "link " + c_uri
        spider_links(c_uri)
      end
    end
  end
end

def down_link(url)
  puts "downloading..." + url
  
  transLength = 0
  totalLength = 0
  partLenght = 1024*64 #the last offset (for the range header)
  
  uri = URI(url)
  fileName = File.basename(uri.path)
  
  Net::HTTP.start(uri.host, uri.port) {|http|
      response = http.head(uri.path)
      totalLength = response['content-length'].to_i
  }
  
  http = Net::HTTP.new(uri.host, uri.port)
  headers = {
    # Content-Range: bytes 2-3/4\r\n
    'Content-Range' => "bytes #{transLength}-#{transLength+partLenght}/#{totalLength}"
  }
  
  downing = Thread.new {
    f = File.new(fileName,"wb+")
    
    http.get(uri.path, headers) do |chunk|
      f.write(chunk)
      f.flush
      
      transLength += chunk.size
      percent = "%.02f"%(transLength*100.0/totalLength)
      printf "\rdowning #{fileName}...#{transLength}-#{transLength+partLenght}/#{totalLength} #{percent}%"
      
    end
    f.close
  }

  while downing.status == "run" or downing.status == "sleep" do
    sleep 0.5
  end

  case downing.status
    when false
      puts "downing normally quit"
    when nil
      puts "downing unnormally quit"
    else
      puts "downing nuknow quit"
  end
  
end

#down_link("http://coderstore.info/RailsShellApplicationin10EasySteps/RailsShellApplicationin10EasySteps(iPhone).m4v")
#down_link("http://coderstore.info/BackgroundProcesseswithRuby/BackgroundProcesseswithRuby.mov")

puts "spider..."
spider_links(ROOT_URI)

puts "downloading..."
# $links.each do | filename, link |
# $links.each do | url |
#   down_link(url)
# end