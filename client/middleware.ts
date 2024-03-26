import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

const protectedPaths = ["/accounts/home", "/accounts/add-database", "/accounts/database", "/accounts/query"];

function isProtectedPath(path: string) {
  for (const protectedPath of protectedPaths) {
    if (path.startsWith(protectedPath)) {
      return true;
    }
  }
  return false;
}

export function middleware(request: NextRequest) {
  const path = request.nextUrl.pathname;
  const token = request.cookies.get("token")?.value
  if(isProtectedPath(path) && !token) {
    return NextResponse.redirect(new URL("/login", request.nextUrl));
  }
}

