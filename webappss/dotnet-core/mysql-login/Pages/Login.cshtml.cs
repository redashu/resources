using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using MyWebApp.Data;
using System.Linq;

namespace MyWebApp.Pages
{
    public class LoginModel : PageModel
    {
        private readonly UserDbContext _context;

        public LoginModel(UserDbContext context)
        {
            _context = context;
        }

        public void OnGet()
        {
        }

        public IActionResult OnPost(string username, string password)
        {
            var user = _context.Users.SingleOrDefault(u => u.Username == username && u.Password == password);

            if (user != null)
            {
                // Redirect to the welcome page after successful login
                return RedirectToPage("/Welcome");
            }
            else
            {
                ViewData["Error"] = "Invalid username or password.";
                return Page();
            }
        }
    }
}

