Rails
====

+ rails new xxx    
+ rake db:create    
+ rails s     

Model
====
+ rails g model urls new    
    + db/migrate/_create_urls.rb    
        t.string :url, :null => false    
    + app/models/url.rb    
        validates url, :presence => true    
    + rails c    
        u = Url.new    
        u.url = "http://google.com"    
        u.save    
        p u    
+ rake db:migrate    
     
Controller    
====
+ rails g controller urls new
    + config/routes.rb    
        resources :urls, :only => [:show, :new, :create]  
    + rake routes    
    + app\controllers\urls_controller.rb    
          def new  
            @shortened_url = Url.new  
          end  
          def create  
            @shortened_url = Url.new(params[:url])  
            if @shortened_url.save  
              flash[:shortened_id] = @shortened_url.id  
              redirect_to new_url_url  
            else  
              render :action => "new"  
            end  
          end  
          def show  
            @shortened_url = Url.find(params[:id])  
            redirect_to @shortened_url.url  
          end
    + remove public/index.html
    + config/routes.rb    
        root :to => redirect('/urls/new')    

View
====
+ app/views/layouts/application.html.haml    
    <% if flash[:shortened_id].present? %>  
    <p class='shortened-link'>  
    The shortened url is available 
    <%= link_to 'here', url_url(flash[:shortened_id]) %>.  
    (Right click and copy link to share it).  
    </p>  
    <% end %>
    
+ app/views/urls/new.html.erb     
    <h1>Add a new URL</h1>  
    <%= form_for @shortened_url do |form| %>  
      <p>  
        <%= form.label :url, "Your URL:" %>  
        <%= form.text_field :url %>  
      </p>  
      <% if @shortened_url.errors[:url].any? %>  
        <p class='error-messages'>  
          The given url <%= @shortened_url.errors[:url].to_sentence %>.  
        </p>  
      <% end %>  
      <p class='buttons'>  
        <%= form.submit "Shorten my URL" %>  
      </p>  
    <% end %>
    
Done
====
+ rails s